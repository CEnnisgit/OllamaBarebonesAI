import ollama


#chat stream example

#res = ollama.chat(
    #model="llama3.2:latest",
    #messages=[
        #{"role": "user", "content": "Pull up a list of books that are similar to the Amazing Spider-Man comics"},
    #],
   # stream=True,
#)

#for chunk in res:
   # print(chunk["message"]["content"], end=" ", flush=True)



#Generate example 
#res = ollama.generate(
    #model="llama3.2:latest",
    #prompt="Pull up a list of books that are similar to Invincible by robert kirkman",
#)


#Show
#print(ollama.show("llama3.2:latest"))


#Create a new model with modelfile 
modelfile = """
From llama3.2:latest
SYSTEM You are very smart librarian, with a bubbly personality, who knows everything about books.
PARAMETER temperature 0.1
"""


#librarian new model example
ollama.create(model="librarianAlpha", system=modelfile, from_= "llama3.2:latest")

res =  ollama.generate(model="librarianAlpha", prompt="Pull up a list of books that are similar to INVINCIBLE by Robert Kirkman")
print(res["response"])
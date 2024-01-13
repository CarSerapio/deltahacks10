import cohere
co = cohere.Client('b4ER3wyquj5jUJlPixZXxm6US0DJR8Nz7GjxsF8p')
with open("transcript.txt") as f:
    data = f.read()
text= data
f.close()
response = co.summarize(
  text=text
)
print(response)
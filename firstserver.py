html="""<!DOCTYPE html>
<html>
  <head>
    <title>Hello!</title>
  </head>  
  <body>
    'Hello Lucca'
    <form action="" method="get" class="form-example">
  <div class="form-example">
    <label for="name">Enter your name: </label>
    <input type="text" name="name" id="name" required>
  </div>
  <div class="form-example">
    <label for="email">Enter your email: </label>
    <input type="email" name="email" id="email" required>
  </div>
  <div class="form-example">
    <input type="submit" value="Subscribe!">
  </div>
</form>
  </body>
</html>"""%name

file=open("username.html","w")
file.write(html)
file.close()
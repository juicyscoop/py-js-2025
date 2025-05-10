## Exercise 1

Write a page that reads two variables from GET: ```start``` and ```end```
(for the sake of simplicity, let's assume that we will only be sending integers).
The page will then output all numbers from ```start``` to ```end```.
If the variables are not transmitted, the page should output a message informing about it.


## Exercise 2

Write a page that loads two variables from a GET: ```width``` and ```height``` (for the sake of simplicity assume that only integers will be sent). Then the page should generate a multiplication table of the given height and width. Use appropriate HTML tags.


## Exercise 3 (*)

Modify exercise 9 from the previous chapter in such a way that after entering a parameter in the URL, the view `/games_played?id=<id>` shows matches played by the team with the given id.


## Exercise 4 (*)

Modify exercise 8 from the previous section so that the name of the club in the table is a link that leads to a page with matches played by the club (the view from the previous exercise).


## Exercise 1

Write a view that, when accessed using the GET method, will display a form accepting a name and a surname.
This form should redirect to the same address using the POST method.
If the page was accessed using POST, the following string should be displayed above the form:
`Hello, <entered name> <entered surname>`.  

Hint: you can use the following code to check which method was used to open the page:
```python
if request.method == "GET":
    do_something()
elif request.method == "POST":
    do_something_else()
```
Hint 2: to make the form redirect to the same page, you can leave its action field empty.


## Exercise 2

Write a view that converts temperature in degrees Celsius to temperature in degrees Fahrenheit (and vice versa). Use the form below:
```html
<form action="" method="POST">
    <label>
        Temperature:
        <input type="number" min="0.00" step="0.01" name="degrees">
    </label>
    <input type="submit" name="conversionType" value="celcToFahr">
    <input type="submit" name="conversionType" value="FahrToCelc">
</form>
``` 

The form has two submit buttons with the same name (the `name` attribute set to the value `conversionType`) but with a different value (the `value` attribute).
To find out which button was pressed, check the value in the `HttpRequest.POST` object under the `conversionType` key. To convert units, use the formulas found [here][degrees-conversion].

**Hint:** The view will be expecting a CSRF token and if it doesn't find it, it will report an error and not let the user further. To prevent this (just for the exercise's sake, because CSRF is a pretty effective protection against hacking the website), use the decorator:

```python
@csrf_exempt
def my_view(request):
    . . . 
```


## Exercise 3 (*)

1. Write a form that takes the following information:
    * football team playing a home match (let it be a drop-down list, where the team ID is the field value, and the name will be the description - load appropriate data from the database),
    * football team playing an away match (as above),
    * score (the easiest way is to do it as two fields - the number of goals scored by one team and by the other).
2. The form should be set to send data to `/add-game/` via POST method.
3. Write a view named `add_game` (share it at URL `/add-game/`) that will:
    * receive data from the form written in the previous section,
    * check if the result data item are correct (if they are valid integers),
    * write the data to the database (using the `Game` model),
    * in case of correct data, it will redirect the user to the page with  matches played by the host team,
    * in case of incorrect data, it will show an error message (in the browser).


## Exercise 4 (*)

Modify the view `/add-game/` so that, based on the score, it modifies the number of points the club has earned:
* for a win: 3 points,
* for a draw: 1 point.

The number of points is kept in the `Teams` table (`Team` model).


## Exercise 5 (*)

Write a view named `modify_team` (share it at URL `/modify-team?id=<id>`) that will:
* retrieve the team ID from the URL,
* create a form with the following fields:
    * team name,
    * number of points scored by the team,
  Fields in this form should be filled with data taken from the database (inputs should have filled the `value` attribute).
  Remember not to allow changing the team ID!
* send the data via POST to the same address,
* upon entering the page via POST, it will receive the data, check if the numbers are correct and modify the team's entry in the database.

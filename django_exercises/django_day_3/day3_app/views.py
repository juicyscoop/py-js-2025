import logging

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


logging.basicConfig(level=logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)

# Create your views here.
def ex1(request, start=None, end=None):
    
    logging.info(f"Received request to /exercise1: start={start}, end={end}, \n request={request}")
    
    if start is None or end is None:
        return HttpResponse("Please provide both start and end values.")
    
    if start > end:
            return HttpResponse("Start value should be less than end value.")

    numbers = list(range(start, end + 1))

    return HttpResponse(", ".join([str(i) for i in numbers]))


def create_html_rows(width, height):
    rows = ""
    for i in range(1, width + 1):
        row = ""
        for j in range(1, height + 1):
            row += f"<td> {i * j} </td>"
        rows += f"<tr> {row} </tr>"
    return rows

def ex2(request, width, height):
    
    logging.info(f"Received request to /exercise2: width={width} height={height}, \n request={request}")
    
    # Schema:
    # 1 | 2 .. | 8
    # 2
    # 3

    rows = create_html_rows(width, height)
    html = f"""
        <title> Multiplication Table </title>
        <h1> Multiplication Table </h1>

        <div>
            <label> Width: {width} </label>
            <label> Height: {height} </label>
        </div>

        <table border="1" cellpadding="5">
            {rows}
        </table>
    """
    return HttpResponse(html)
    

@csrf_exempt
def forms_ex1(request):
    if request.method == "GET":
        # Zobraz formular
        html = """
        <form method="POST">
            <label>
                Name:
                <input type="text" name="name">
            </label>
            <label>
                Surname:
                <input type="text" name="surname">
            </label>
            <input type="submit">
        </form>
        """
        return HttpResponse(html)
    elif request.method == "POST":
        # Zpracuj formular
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        return HttpResponse(f"Hello {name} {surname}")
    

@csrf_exempt
def forms_ex2(request):
    html = """
    <form action="" method="POST">
        <label>
            Temperature:
            <input type="number" min="0.00" step="0.01" name="degrees">
        </label>
        <input type="submit" name="conversionType" value="celcToFahr">
        <input type="submit" name="conversionType" value="FahrToCelc">
    </form>
    """
    if request.method == "GET":
        return HttpResponse(html)
    elif request.method == "POST":
        incoming_value = request.POST.get("degrees")
        conversion_type = request.POST.get("conversionType")
        if conversion_type == "celcToFahr":
            outgoing_value = (float(incoming_value) * 1.8) + 32
        elif conversion_type == "FahrToCelc":
            outgoing_value = (float(incoming_value) - 32) / 1.8
        else:
            raise NotImplementedError

    out = f"""
    Converted incoming value {incoming_value} to {outgoing_value}.
    Conversion type was {"Celsius to Fahrenheit" if conversion_type == "celcToFahr" else "Fahrenheit to Celsius"}.
    """
    return HttpResponse(out)




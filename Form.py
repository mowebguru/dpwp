# class for blank form.
class Subscribe(object):
    def __init__(self):
        self.title = "Registration Form"
        self.style = "css/formstyle.css"
        self.bootstrap = "css/bootstrap.min.css"
        self.head = """<!DOCTYPE html>
<html>
<head>
    <title>{self.title}</title>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <meta name="author" content="@mokamara">
    <link href="{self.style}" rel="stylesheet" type="text/css">
    <link href="{self.bootstrap}" rel="stylesheet" type="text/css">
</head>
<body>"""
        self.form = """

<div class="container-fluid">
    <div id="header" align="center">
        <h2>A&Z DAYCARE</h2>
        <img src="images/daycare1.jpg" class="img-rounded" alt="A&Z DAYCARE" ><br />
    </div><br />
    <!-- Create Contact form-->

    <div id="clientform" align="center" class="form-group">
        <form action="" id="add" method="GET" name="contact-form">
            <fieldset>
                <legend></legend>
                <p><strong>Welcome to A&Z DAYCARE. Please provide the below information and someone will get back to you as soon either
                 by phone or email</strong>.</p>
                <input type="text"  name="firstname" placeholder="First Name" required autofocus ><br />
                <input type="text" name="lastname" placeholder="Last Name" required ><br />
                <input type="tel" name="phone" placeholder="Phone Number" required><br />
                <input type="email" name="email" placeholder="Email" ><br />
                <input type="text" name="profession" placeholder="profession..." ><br />
                <p><h3>What's your gender?</h3><input type="radio" name="gender" value="male" checked> MALE
                <input type="radio" name="gender" value="female"> FEMALE<br></p>
                <p><h3>Please select package below:</h3>
                <select name="package" class="form-control" style="width:280px;">
                  <option value="daily">Daily</option>
                  <option value="weekly">Weekly</option>
                  <option value="bi-weekly">Bi-weekly</option>
                  <option value="monthly">Monthly</option>
                </select></p>
                <input name="submit" type="submit" value="Submit"><br />
                """
        self.close = """
            </fieldset>
        </form><br />
    </div><br />
    <hr>

    <div>

    </div>

</div>

</body>
</html>"""
    #print the components fo the form.
    def print_info(self):
        info = self.head + self.form + self.close
        info = info.format(**locals())
        return info


    def print_data(self,firstname,lastname,phone,email, profession, package):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.profession = profession
        self.package = package
        inquiryinfo = """
<!DOCTYPE html>
<html>
<head>
    <title>Confirmation</title>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <meta name="author" content="@mokamara">
    <link href="css/formstyle.css" rel="stylesheet" type="text/css">
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css">
</head>
<body>
<div class="wrapper">

<div id="header" align="center">
        <h2>A&Z DAYCARE</h2>
        <img src="images/daycare1.jpg" class="img-rounded" alt="A&Z DAYCARE" ><br />
        <hr>
        </div>
        <div id="inquiryform">
    <br/><h3>Hello {}:</h3></br>
            <p>
            Thanks for inquiring about services at A&Z DAYCARE, LLC. A representative will contact shortly with more details.
            As you indicated on the inquiry for, we would like to confirm <strong> {} </strong> as family name; the best number to
            reach you is <strong>{} </strong>. We will add you to our contact list using this email <strong>{} </strong>
             for official communications.<br />
            <p>You also indicated that you are <strong>{} </strong> by profession, and and the select package is <strong> {} </strong> package. <br/>

            <p>The Management <br />
            <p>A&Z Day Care
    </div>
</div>
</body>
</html>"""
        info_output= inquiryinfo
        info_output = info_output.format(firstname, lastname, phone, email, profession, package) #populate data submitted through URL
        return info_output
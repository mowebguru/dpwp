'''Name   : Mohamed A. KAMARA
   Course : Design Patterns for Web Programming - Online
   File   : Week 3 - Reusable Code
   Date   :Sept. 15, 2016'''

# this class holds the design for the loan application  - name, email, credit score, loan amount, loan duration
class FormPage(object):
    def __init__(self):
        self.title = "Loan Application"
        self.style = "css/style.css"
        self.header = """
        <!DOCTYPE html>
<html>
<head>
    <title>Loan Appraisal</title>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <meta name="author" content="@mokamara">
    <link href="{self.style}" rel="stylesheet" type="text/css">
</head>"""
        self.formbody = """
<body>
    <div id="header" align="center">
            <div class="appraisal-page">
                        <img src="images/autoloan.jpg" class="img-rounded" alt="Sansan Auto Sales" >
                <h3 align="left">No Credit! Bad Credit!</h3>
                <p align="left">At Sansan Auto Sales, every customer walks away with a car. Please fill out the application below and a representative will contact you. </p>

              <div class="form">
                <form class="appraisal-form">
                  <fieldset>
                      <legend>Application Details</legend>
                          <input type="text" name="name" placeholder="full name goes here..." required/>
                          <input type="email" name="email" placeholder="email address" />
                          <input type="number" name="rate" placeholder="What is the interest rate?" min="1" max="30" required/>
                          <input type="number" name="amount" placeholder="how much is the car?" min="1000" max="100000" required/>
                          <input type="number" name="term" placeholder="months needed to pay off loan?" min="12" max="60" required/>
                          <button name="apply" type="submit">Submit</button>
                          """
        self.formclose = """
                  </fieldset>
                </form>
              </div>
            </div>
        </div>
</body>
</html>"""

        #this module prints the various components fo the loan application form.
    def print_info(self):
        theform = self.header + self.formbody + self.formclose
        theform = theform.format(**locals())
        return theform

# class for the loan application

class ResultPage(object):
    def __init__(self):
        self.title = "Loan Approval"
        self.style = "css/style.css"

        #define function to print result page
    def print_result(self, name, monthlyLoan, payoutAmount, totInterest, loanperiod, email):
        resultpage = """
        <!DOCTYPE html>
<html>
<head>
    <title>Loan Approval</title>
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <meta name="author" content="@mokamara">
    <link href="css/style.css" rel="stylesheet" type="text/css">
</head>
<body>
    <div id="header" align="center">
            <div class="appraisal-page">
                        <img src="images/autoloan.jpg" class="img-rounded" alt="Sansan Auto Sales" >
                <h3 align="left">Dear {} </h3>
                <p align="left">Thanks for applying for an auto loan financing with Sansan Auto Sales. Based on the information provided, your loan details are as follows: </p>
                <div class="row">
    <div class="col-md-12 padding-left-none padding-right-none">
        <table class="table table-condensed summary-section">
            <tbody>
                <tr>
                    <td><strong><span class="float-left summary-section-desc">Monthly Payment : </span><span class="float-right">${}</span></strong></td>
                </tr>
                <tr>
                    <td><strong><span class="float-left summary-section-desc">Payout Amount :</span><span class="float-right" >${}</span></strong></td>
                </tr>
                <tr>
                    <td><strong><span class="float-left summary-section-desc">Accrued Interest : </span><span class="float-right">${}</span></strong></td>
                </tr>
                <tr>
                    <td><strong><span class="float-left summary-section-desc">Loan Duration (years) :</span><span class="float-right">{}</span></strong></td>
                </tr>

            </tbody>
        </table>
    </div>
                    <p align="left">For future communication, we will contact you using <strong>{}</strong> provided during your application. </p>
                    <p align="left">The Management </p>
</div>



</body>
</html>
"""
        result = resultpage
        result = result.format(name, monthlyLoan, payoutAmount, totInterest, loanperiod,email)
        return result


'''Name   : Mohamed A. KAMARA
   Course : Design Patterns for Web Programming - Online
   File   : Week 4 - Dynamic Site
   Date   :Sept. 23, 2016'''

class Page(object):
    def __init__(self):
        self.title = "F&G Beauty Supply"
        self.head ='''
        <!DOCTYPE html>
<html lang="en">
    <head>
        <title>{self.title}</title>
        <meta name="keywords" content="" />
		<meta name="description" content="" />
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Google Web Font Embed -->
        <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,300italic,400italic,600,600italic,700,700italic,800,800italic' rel='stylesheet' type='text/css'>

        <!-- Bootstrap core CSS -->
        <link href="css/bootstrap.css" rel='stylesheet' type='text/css'>
        <link href="js/colorbox/colorbox.css"  rel='stylesheet' type='text/css'>
        <link href="css/style.css"  rel='stylesheet' type='text/css'>

        <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
          <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
        <![endif]-->
    </head>
    '''
        self.body = '''

    <body>

        <div class="dynamic-top-bar" id="dynamic-top">
            <div class="container">
                <div class="subheader">
                    <div id="phone" class="pull-left">
                            <img src="images/phone.png" alt="phone"/>
                            612-916-2572
                    </div>
                    <div id="email" class="pull-right">
                            <img src="images/email.png" alt="email"/>
                            mowebguru@gmail.com
                    </div>
                </div>
            </div>
        </div>
        <div class="dynamic-top-menu">
            <div class="container">
                <!-- Static navbar -->
                <div class="navbar navbar-default" role="navigation">
                    <div class="container">
                        <div class="navbar-header">
                                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                </button>

                        </div>
                        <div class="navbar-collapse collapse" id="dynamic-nav-bar">
                            <ul class="nav navbar-nav navbar-right" style="margin-top: 40px;">
                                <li class="active"><a href="#dynamic-top">Home</a></li>
                                <li><a href="?hair=brazilian">Brazilian</a></li>
                                <li><a href="?hair=indian">Indian</a></li>
                                <li><a href="?hair=peruvian">Peruvian</a></li>
                                <li><a href="?hair=malaysian">Malaysian</a></li>
                                <li><a href="?hair=african">African</a></li>
                            </ul>
                        </div><!--/.nav-collapse -->
                    </div><!--/.container-fluid -->
                </div><!--/.navbar -->
            </div> <!-- /container -->
        </div>

        <div>
            <!-- Carousel -->
            <div id="dynamic-carousel" class="carousel slide" data-ride="carousel">
                <!-- Indicators -->
                <ol class="carousel-indicators">
                    <li data-target="#dynamic-carousel" data-slide-to="0" class="active"></li>
                    <li data-target="#dynamic-carousel" data-slide-to="1"></li>
                    <li data-target="#dynamic-carousel" data-slide-to="2"></li>
                </ol>
                <div class="carousel-inner">
                    <div class="item active">
                        <div class="container">
                            <div class="carousel-caption">
                                <h1>WELCOME TO F&G Beauty Supply</h1>
                                <p>CHOOSE THE ONE SUITABLE FOR YOU</p>
                                <p><a class="btn btn-lg btn-green" href="#" role="button" style="margin: 20px;">Virgin Human Hair</a>
                                	<a class="btn btn-lg btn-orange" href="#" role="button">Synthetic Hair</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="item">
                        <div class="container">
                                <div class="carousel-caption">
                                    <div class="col-sm-6 col-md-6">
                                    	<h1>AUTHENTIC</h1>
                                        <p>Human Hair offers the most natural look and feel It is remarkably soft with a shine and movement that is not easily duplicated in synthetic hair. </p>
                                    </div>
                                    <div class="col-sm-6 col-md-6">
                                    	<h1>NATURAL</h1>
                                        <p>Human Hair can be cut and styled to suit your personal tastes And while it can be a more expensive pick Human Hair is by far the superior choice if quality is the only consideration.</p>
                                    </div>
                                </div>
                        </div>
                    </div>

                </div>
                <a class="left carousel-control" href="#dynamic-carousel" data-slide="prev"><span class="glyphicon glyphicon-chevron-left"></span></a>
                <a class="right carousel-control" href="#dynamic-carousel" data-slide="next"><span class="glyphicon glyphicon-chevron-right"></span></a>
            </div><!-- /#dynamic-carousel -->
        </div>

        <div class="dynamic-team" id="dynamic-about">
            <div class="container">
                <div class="row">
                    <div class="dynamic-line-header">
                        <div class="text-center">
                            <hr class="team_hr team_hr_left"/><span>Our Products</span>
                       '''
        self.close = '''
                        </div>

                        </div>

                    </div>
                </div>
                <div class="clearfix"> </div>

            </div>
        </div><!-- /.dynamic-team -->

                </div>

        </div> <!-- /.dynamic-portfolio -->

        <div class="dynamic-footer" >
            <div class="container">
                <div class="row">
                    <div class="text-center">

                        <div class="footer_bottom_content">
                   			<span id="footer-line">Copyright 2016 F&nbsp;G Beauty Supply<a href="#"></a></span>
                        </div>

                    </div>
                </div>
            </div>
        </div>

        <script src="js/jquery.min.js" type="text/javascript"></script>
        <script src="js/bootstrap.min.js"  type="text/javascript"></script>
        <script src="js/stickUp.min.js"  type="text/javascript"></script>
        <script src="js/colorbox/jquery.colorbox-min.js"  type="text/javascript"></script>
        <script src="js/dynamic_script.js"  type="text/javascript"></script>
		<!-- dynamic 395 urbanic -->
    </body>
</html>'''

        def print_page(self):
            allPages = self.head + self.body + self.close
            allPages = allPages.format(**locals())
            return allPages

class ContentPage(Page):
    def __init__(self):
        #   constructor function for the super class
        super(ContentPage,self).__init__()
        self.content = '''
            <table id="product-attribute-specs-table" class="table table-bordered table-responsive" style="width: 869px; height: 386px;">
<tbody>
    <tr><th style="text-align: left;">CATEGORY:</th>
<td class="data" style="text-align: left;"><strong><span>{}</span></strong></td>
</tr
    <tr><th style="text-align: left;">Sample</th>
    <td class="data" style="text-align: center;"><span><img src="{}" alt="{}" height="350" width="380"></span></td>
    </tr>
<tr><th style="text-align: left;">Price:</th>
<td class="data" style="text-align: left;"><span>{}</span></td>
</tr
<tr><th style="text-align: left;">Hair Color:</th>
<td class="data" style="text-align: left;"><span>{}</span></td>
</tr>
<tr><th style="text-align: left;">Hair Length:</th>
<td class="data" style="text-align: left;"><span>{}</span></td>
</tr>
<tr><th style="text-align: left;">Texture:</th>
<td class="data" style="text-align: left;"><span>{}</span></td>
</tr>
<tr><th style="text-align: left;">Hair Weight:</th>
<td class="data" style="text-align: left;"><span>{}</span></td>
</tr>
<tr><th style="text-align: left;">Quality:</th>
<td class="data" style="text-align: left;"><span>{}</span></td>
</tr>
<tr><th style="text-align: left;"><span><span>Description:</span></th>
<td class="data" style="text-align: left;">{}</td>
</tr>
</tbody>
</table>'''

    def print_Content(self, name, image,price,color,length,texture,weight,quality,description):
        allcontent = self.head + self.body + self.content + self.close
        allcontent = allcontent.format(name, image,price,color,length,texture,weight,quality,description)
        return allcontent


    def print_Page(self):
        allPages = self.head + self.body + self.close
        allPages = allPages.format(**locals())
        return allPages


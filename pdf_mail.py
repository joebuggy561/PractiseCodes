from pdf_mail import sendpdf
 
 
# Create an object of sendpdf function
my_job_app_mail = sendpdf("josephnwanijr@gmail.com",#"##sender##email",
                "josephnwanijr@outlook.com",#"###receiveremail###",
                "*****************",#"##senderemailpassword##",
                "mycv",#"##subject of message###",
                "this is my cv",#"##bodyofmessage###",
                "CV.pdf",#"###filename###",
                "C:/Users/user/Desktop/git/py/100dayscd/CV.pdf")#"###pathoffile###")
 
# sending an email
my_job_app_mail.email_send()

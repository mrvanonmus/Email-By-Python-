
طباعة ( "" + عمود )
طباعة ( "__ __ _______ __" + co )
طباعة ( "| \ / | __ \ \ / /" + co )
طباعة ( "| \ / | | __) \ \ / /" + l )
طباعة ( "| | \ / | | _ / \ \ / /" + h )
طباعة ( "| | | | | \ \ /" + عمود )
طباعة ( "| _ | | _ | _ | \ _ \ \ / \ n \ n \ n " + c )
طباعة ( "______________________________" )
print ( "My Chanel: قيس الحموي" )
طباعة ( "______________________________" )
print ( "My Insta: asta al0hmawi" )import smtplib
sender = input(" Enter your Email : ")
password = input("Enter the Password : ")
receiver = input("Enter your Receiver : ")
message =input ("Enter your Message : ")
try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender,password)
        server.sendmail( sender ,receiver,  message)
        server.quit()
        print(' sent Successfully')
except:
        print(' there is error ')

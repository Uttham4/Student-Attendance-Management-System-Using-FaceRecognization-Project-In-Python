import os
import yagmail

receiver = "kamaraj4444q@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance/Attendance_.csv"  # attach the file

# mail information
yag = yagmail.SMTP("utthamsingh101@gmail.com", "spcg vuuh bgxj sxmf")

# sent the mail

yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)

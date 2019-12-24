site = "http://www.vairous7x.com/admin123/"
###################
pas = ['123/','admin/','admin123/','admin12345/']
###################
target = input ("Enter WebSite Target====> ")
###################
for t in pas:
  website = target+t
  if website == site:
    print ("Admin Login Page Is==> ",website)
  else:
    print ("Admin Login Page Not Found...!")
###############################
##### CODED BY VAIROUS 7X #####
###############################

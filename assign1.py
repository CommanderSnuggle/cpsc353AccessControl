user_permissions = {}
role_permissions = {}

with open("ura.txt") as f:
    for line in f:
      name = line.split(' ')[0].strip().lower()
      roles = line.split(' ')[1].strip().lower()
      if name not in user_permissions.keys():
        user_permissions.update({name:{"roles":[roles]}})
      else:
        user_permissions[name]["roles"].append(roles)

with open("pra.txt") as f:
    for line in f:
      cleanLine = line.strip() # remove \n from the lines
      role = line.split(' ')[0].strip().lower()
      permissions = cleanLine.split(' ')[1].lower()
      object_access = cleanLine.split(' ')[2].lower()
      if role not in role_permissions.keys():
        role_permissions.update({role: {"perms":{permissions: [object_access]}}})
      else:
        if permissions not in role_permissions[role]['perms'].keys():
          role_permissions[role]['perms'].update({permissions: [object_access]})
        else: 
          role_permissions[role]['perms'][permissions].append(object_access)

def getPermissions(roles): #roles is an array of role that a logged in user has
  permissions = [] # is an array to be filled with commands a user can send
  for role in roles:
      for actions in role_permissions[role]['perms']:
        for object_of_action in role_permissions[role]['perms'][actions]:
          permissions.append('{0} {1}'.format(actions, object_of_action))
  return permissions

def unauth_script():
  print("                         /    |")
  print("                         /     |")
  print(" You shall not pass!    /      |")
  print("                       /       |")
  print("          \       ___,'        |")
  print("                <  -'          :")
  print("                 `-.__..--'``-,_\_")
  print("                    |o/ <o>` :,.)_`>")
  print("                    :/ `     ||/)")
  print("                    (_.).__,-` |\\")
  print("                    /( `.``   `| :")
  print("                    \'`-.)  `  ; ;")
  print("                    | `       /-<")
  print("                    |     `  /   `.")
  print("    ,-_-..____     /|  `    :__..-'\\")
  print("   /,'-.__\\  ``-./ :`      ;       \\")
  print("   `\ `\  `\\  \ :  (   `  /  ,   `. \\")
  print("     \` \   \\   |  | `   :  :     .\ \\")
  print("      \ `\_  ))  :  ;     |  |      ): :")
  print("     (`-.-'\ ||  |\ \   ` ;  ;       | |")
  print("      \-_   `;;._   ( `  /  /_       | |")
  print("       `-.-.// ,'`-._\__/_,'         ; |")
  print("          \:: :     /     `     ,   /  |")
  print("           || |    (        ,' /   /   |")
  print("           ||                ,'   /    |")

uname = str(input("login: "))

if uname in user_permissions:
  roles = user_permissions[uname]["roles"]
  print("Welcome! " + uname)
  ucmd = str(input("cmd>"))
  while ucmd != "exit":
    commandsAllowed = getPermissions(roles)
    if ucmd.lower() in commandsAllowed:
      print('Access granted by virtue of roles: ' + str(roles))
    else:
      unauth_script()
      print("Access denied: you are not authorized to perform this action!")
    ucmd = str(input("cmd>"))
  print("Program has ended")
else:
  print("ERROR: user " +uname+" is not in the database!")
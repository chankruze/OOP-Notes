try:
    file_name = "hello_world.txt"
    file_operation= 'r'
    f_hello = open(file_name, file_operation)
    f_hello.write("Test write to hello world file !")

except IOError:
    print("ERROR : Unable to write data in '{}' beacuse opened in '{}' mode !".format(file_name, file_operation))
    print("Change file operation to 'r+' or 'w' mode.")
# else:
#     print("Success !")
#     f_hello.close()
finally:
    print("I always work no matter what errors occur !")

#site connect check
import urllib.request
import socket

url = input("Enter the URL: ")
try:
    urllib.request.urlopen(url)
    print("The site is up and running")
except urllib.error.URLError as e:
    print("The site is down")
    print(e.reason)
except socket.gaierror:
    print("The site is down")
    print("The site is not reachable")
except ConnectionError:
    print("The site is down")
    print("Connection error")
except TimeoutError:
    print("The site is down")
    print("Timeout error")
except Exception as e:
    print("The site is down")  # Inform the user that an error has occurred
    print(e)  # Print the exception message
    print(type(e))  # Print the type of the exception
    print(e.args)  # Print the arguments that were passed to the exception
    print(e.with_traceback)  # Print the traceback method (not called)
    print(e.with_traceback())  # Print the traceback (called)
    print(e.__traceback__)  # Print the traceback object
    print(e.__traceback__.tb_lineno)  # Print the line number where the exception occurred
    print(e.__traceback__.tb_frame)  # Print the current stack frame
    print(e.__traceback__.tb_frame.f_locals)  # Print local variables in the current frame
    print(e.__traceback__.tb_frame.f_globals)  # Print global variables in the current frame
    print(e.__traceback__.tb_frame.f_code)  # Print the code object of the current frame
    print(e.__traceback__.tb_frame.f_code.co_name)  # Print the name of the function where the error occurred
    print(e.__traceback__.tb_frame.f_code.co_filename)  # Print the filename where the error occurred
    print(e.__traceback__.tb_frame.f_code.co_firstlineno)  # Print the first line number of the code object
    print(e.__traceback__.tb_frame.f_code.co_argcount)  # Print the number of arguments the function takes
    print(e.__traceback__.tb_frame.f_code.co_varnames)  # Print variable names in the function
    print(e.__traceback__.tb_frame.f_code.co_flags)  # Print the flags of the code object
    print(e.__traceback__.tb_frame.f_code.co_consts)  # Print constants used in the code
    print(e.__traceback__.tb_frame.f_code.co_names)  # Print names used in the code
    print(e.__traceback__.tb_frame.f_code.co_freevars)  # Print free variables in the code
    print(e.__traceback__.tb_frame.f_code.co_cellvars)  # Print cell variables in the code
    print(e.__traceback__.tb_frame.f_code.co_stacksize)  # Print the stack size
    print(e.__traceback__.tb_frame.f_code.co_lnotab)  # Print line number mapping


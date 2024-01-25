## 0x10. Python - Network #0

### Description

This project covers various aspects of network programming using Python and Bash scripting. It involves sending HTTP requests, handling responses, understanding HTTP methods, headers, cookies, and more. The project includes a series of tasks designed to reinforce understanding and proficiency in network protocols and communication.

### General Information

- **Author:** Guillaume
- **Weight:** 1
- **Project Duration:** Jan 25, 2024, 6:00 AM - Jan 26, 2024, 6:00 AM
- **Checker Release Date:** Jan 25, 2024, 12:00 PM
- **Auto Review Launch:** Scheduled at the deadline

### Resources

- HTTP (HyperText Transfer Protocol) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
- HTTP Cookies

### Learning Objectives

Upon completion of this project, learners should be able to explain the following concepts without external assistance:

- Understanding of URLs, HTTP, and HTTP requests/responses
- Reading URLs and understanding their components
- Differentiating between HTTP methods, status codes, headers, and cookies
- Making requests using cURL and interpreting responses
- Understanding the process when typing a URL in a browser

### Requirements

- All scripts should be tested on Ubuntu 20.04 LTS.
- Bash scripts should be exactly 3 lines long and end with a new line.
- All files must be executable and use `#!/bin/bash` as the first line for Bash scripts.
- Python scripts should use `#!/usr/bin/python3` as the first line and adhere to PEP8 style guidelines.
- All modules, classes, and functions should be properly documented.
- No plagiarism or content publishing is allowed.

### Tasks

| Task | Description | Script |
| ---- | ----------- | ------ |
| 0 | cURL body size | [0-body_size.sh](https://github.com/alx-higher_level_programming/0x10-python-network_0/0-body_size.sh) |
| 1 | cURL to the end | [1-body.sh](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0/1-body.sh) |
| 2 | cURL Method | [2-delete.sh](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0/2-delete.sh) |
| 3 | cURL only methods | [3-methods.sh](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0/3-methods.sh) |
| 4 | cURL headers | [4-header.sh](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0/4-header.sh) |
| 5 | cURL POST parameters | [5-post_params.sh](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0/5-post_params.sh) |
| 6 | Find a peak | [6-peak.py](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0/6-peak.py), [6-peak.txt](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0/6-peak.txt) |
| 7 | Only status code | [100-status_code.sh](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0/100-status_code.sh) |
| 8 | cURL a JSON file | [101-post_json.sh](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0/101-post_json.sh) |
| 9 | Catch me if you can! | [102-catch_me.sh](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0/102-catch_me.sh) |

**Note:** All scripts should be tested using the provided sandbox with the web server running on port 5000.

For further details and implementations, please refer to the respective script files in the [GitHub repository](https://github.com/Desire-2/alx-higher_level_programming/0x10-python-network_0) associated with this project.


### Tasks

#### Task 0: cURL body size

This task requires writing a Bash script that takes a URL as input, sends a request to the URL, and displays the size of the response body in bytes using `curl`.

- **Script**: [0-body_size.sh](https://github.com/alx-higher_level_programming/0x10-python-network_0/0-body_size.sh)
- **Example Output**:
  ```bash
  guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
  10
  guillaume@ubuntu:~/0x10$
  ```

#### Task 1: cURL to the end

In this task, a Bash script is written to take a URL as input, send a GET request to the URL, and display the body of the response for a 200 status code using `curl`.

- **Script**: [1-body.sh](https://github.com/alx-higher_level_programming/0x10-python-network_0/1-body.sh)
- **Example Output**:
  ```bash
  guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
  Route 2
  guillaume@ubuntu:~/0x10$
  ```

#### Task 2: cURL Method

This task involves writing a Bash script that sends a DELETE request to the URL provided as the first argument and displays the body of the response using `curl`.

- **Script**: [2-delete.sh](https://github.com/alx-higher_level_programming/0x10-python-network_0/2-delete.sh)
- **Example Output**:
  ```bash
  guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
  I'm a DELETE request
  guillaume@ubuntu:~/0x10$
  ```

#### Task 3: cURL only methods

For this task, a Bash script is required to take a URL as input and display all the HTTP methods that the server will accept using `curl`.

- **Script**: [3-methods.sh](https://github.com/alx-higher_level_programming/0x10-python-network_0/3-methods.sh)
- **Example Output**:
  ```bash
  guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
  OPTIONS, HEAD, PUT
  guillaume@ubuntu:~/0x10$
  ```

#### Task 4: cURL headers

In this task, a Bash script should be written to take a URL as an argument, send a GET request to the URL with a custom header `X-School-User-Id: 98`, and display the body of the response using `curl`.

- **Script**: [4-header.sh](https://github.com/alx-higher_level_programming/0x10-python-network_0/4-header.sh)
- **Example Output**:
  ```bash
  guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
  Hello School!
  guillaume@ubuntu:~/0x10$
  ```

#### Task 5: cURL POST parameters

For this task, a Bash script is needed to take a URL as input, send a POST request to the URL with specified parameters, and display the body of the response using `curl`.

- **Script**: [5-post_params.sh](https://github.com/alx-higher_level_programming/0x10-python-network_0/5-post_params.sh)
- **Example Output**:
  ```bash
  guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
  POST params:
      email: test@gmail.com
      subject: I will always be here for PLD
  guillaume@ubuntu:~/0x10$
  ```

#### Task 6: Find a peak

This task involves writing a Python function that finds a peak in a list of unsorted integers. The function should have the lowest complexity and must not use any import statements.

- **Script**: [6-peak.py](https://github.com/alx-higher_level_programming/0x10-python-network_0/6-peak.py), [6-peak.txt](https://github.com/alx-higher_level_programming/0x10-python-network_0/6-peak.txt)
- **Example Output**:
  ```python
  # Sample function usage
  print(find_peak([1, 2, 4, 6, 3]))  # 6
  print(find_peak([4, 2, 1, 2, 3, 1]))  # 4
  print(find_peak([2, 2, 2]))  # 2
  print(find_peak([]))  # None
  print(find_peak([-2, -4, 2, 1]))  # 2
  print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # 4
  ```
  Complexity: O(log(n)), O(n), O(nlog(n)), or O(n^2).

#### Task 7: Only status code (Advanced)

This task requires writing a Bash script that sends a request to a URL provided as an argument and displays only the status code of the response. No pipes, redirections, semicolons, or `&&` operators are allowed, and only `curl` should be used.

- **Script**: [100-status_code.sh](https://github.com/alx-higher_level_programming/0x10-python-network_0/100-status_code.sh)

#### Task 8: cURL a JSON file (Advanced)

For this task, a Bash script should be created to send a JSON POST request to a URL provided as the first argument. The body of the request should contain the contents of a file provided as the second argument. The script should use `curl` and validate if the content of the file is valid JSON.

- **Script**: [101-post_json.sh](https://github.com/alx-higher_level_programming/0x10-python-network_0/101-post_json.sh)

#### Task 9: Catch me if you can! (Advanced)

In this task, a Bash script is required to make a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing "You got me!" in the body of the response. Only `curl` should be used.

- **Script**: [102-catch_me.sh](https://github.com/alx-higher_level_programming/0x10-python-network_0/102-catch_me.sh)

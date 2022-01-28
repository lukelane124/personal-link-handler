#!/bin/env python3
import os
import sys
from urllib.parse import *

parsed_url = urlparse(sys.argv[1])
#print(raw_data)
if parsed_url.scheme == "tll":
	operation = parsed_url.netloc
	if (operation == "open"):
		print("open")
		parsed_query = parse_qs(parsed_url.query)
		print(parsed_query)
		application = parsed_query["application"][0]
		print(f"{application=}")
		args = parsed_query["args"][0]
		print(args)
		#subprocess.call([application], args)
		os.system(f"{application} {args}")
		#print(type(parsed_query))
		#application_string_raw = parsed_query
		

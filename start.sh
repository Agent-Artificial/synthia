#!/bin/bash



comx module serve validator.text_validator.TextValidator text_validator.TextValidator --ip 0.0.0.0 --port 8080 --subnets-whitelist 3 --blacklist vali::COMTOAWEL





comx module register text_validator.TextValidator 0.0.0.0 8080 validator.text_validator.TextValidator --netuid 3 --stake 5202.5
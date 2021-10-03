REGEX_EMAIL = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
REGEX_GIT_PROJECT = r'((git@|http(s)?:\/\/)([\w\.@]+)(\/|:))([\w,\-,\_]+)\/([\w,\-,\_]+)(.git){0,1}((\/){0,1})'
REGEX_VERSION_NUMBER = r'^(\d+)((\.{1}\d+)*)(\.{0})$'
REGEX_FILE_PY = r'[a-zA-Z0-9/\\]{,100}(.py)$'
REGEX_FILE = r'([a-zA-Z0-9/\\])+((.[a-zA-Z])+)'


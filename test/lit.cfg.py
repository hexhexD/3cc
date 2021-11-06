import lit.formats

config.name = "mycc"

# So lit doesn't look for bash.exe on my machine
config.test_format = lit.formats.ShTest(False)

config.suffixes = ['.c', '.txt']
config.excludes = ['CMakeLists.txt']

config.test_source_root = os.path.dirname(__file__)
config.test_exec_root = os.path.join(config.mycc_obj_root, 'test')

config.substitutions.append(('%3cc',
    os.path.join(config.mycc_obj_root, "3cc")))
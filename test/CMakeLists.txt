configure_file(lit.site.cfg.py.in lit.site.cfg.py @ONLY)
configure_file(FileCheck.exe FileCheck.exe COPYONLY)
configure_file(not.exe not.exe COPYONLY)

add_custom_target(check
	COMMAND ${LIT} -v .
	WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
	DEPENDS 3cc
	)
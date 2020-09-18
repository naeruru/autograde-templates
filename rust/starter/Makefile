.PHONY: archive clean


archive: 
	@make clean ; tar czf project_name.tar.gz *

clean:
	@rm -R *.tar.gz *.pyc __pycache__ *~* *#* */*~* */*#* .DS_Store || true
	@find . -type d -name target -prune -exec rm -rf {} \;

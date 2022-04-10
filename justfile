default:
	@just --list

build:
	@./build.py

run:
	@just build
	@firefox index.html

clean:
	@rm *.html

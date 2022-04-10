default:
	@just --list

build:
	@./build.py

run:
	@just build
	@firefox index.html

clean:
	@rm *.html

publish:
	@just build
	@git add *.html
	@git commit -m "Published a new article!" -a
	@git push

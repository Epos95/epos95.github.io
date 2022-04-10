# Prints this list!
default:
	@just --list

# Generates all html files for the blog!
build:
	./build.py

# Builds and opens the blog in firefox
run:
	@just build
	firefox index.html

# Removes all generated html files
clean:
	rm *.html

# Only for usage when publishing a new article!
publish:
	@just build
	git add *.html
	git commit -m "Published a new article!" -a
	git push
	@just clean

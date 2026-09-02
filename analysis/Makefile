.PHONY: ci format lint typecheck test emtsv-up emtsv-down
ci: format lint typecheck test
format:
	uv run ruff format --check src tests
lint:
	uv run ruff check src tests
typecheck:
	uv run ty check src
test:
	uv run pytest --doctest-modules --cov=karogasok_temak --cov-report=term-missing

# emtsv runs as a service. The first request after start pays ~40s to load the
# morphological analyser; everything after that is fast.
emtsv-up:
	docker run --rm -d --name emtsv -p 5000:5000 mtaril/emtsv
emtsv-down:
	docker stop emtsv

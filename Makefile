PYTHON ?= python3

.PHONY: solutions source analysis diagrams
solutions:
	$(PYTHON) "Sec B/scripts/build.py"

source:
	$(PYTHON) "Sec B/scripts/build.py" --source-only

analysis:
	$(PYTHON) "Sec B/scripts/inventory.py"
	$(PYTHON) "Sec B/scripts/build_reports.py"

diagrams:
	$(PYTHON) "Sec B/scripts/build.py" --diagrams

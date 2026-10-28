PYTHON ?= python3

.PHONY: solutions solutions-a solutions-b source analysis diagrams
solutions: solutions-b solutions-a

solutions-a:
	$(PYTHON) "Sec A/scripts/build.py"

solutions-b:
	$(PYTHON) "Sec B/scripts/build.py"

source:
	$(PYTHON) "Sec B/scripts/build.py" --source-only
	$(PYTHON) "Sec A/scripts/build.py" --source-only

analysis:
	$(PYTHON) "Sec B/scripts/inventory.py"
	$(PYTHON) "Sec B/scripts/build_reports.py"
	$(PYTHON) "Sec A/scripts/build_reports.py"

diagrams:
	$(PYTHON) "Sec B/scripts/build.py" --diagrams
	$(PYTHON) "Sec A/scripts/build.py" --diagrams

from pathlib import Path

from ome_types_widget import widget

EXAMPLE_XML = Path(__file__).parent / "example.ome.xml"


def test_widget(qtbot):
    widget.OMETree(str(EXAMPLE_XML))

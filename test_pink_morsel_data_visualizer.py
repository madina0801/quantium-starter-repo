from pink_morsel_data_visualizer import app

def test_header_is_present(dash_duo):
	dash_duo.start_server(app)
	dash_duo.find_element("#header", timeout=10)

def test_visualization_is_present(dash_duo):
	dash_duo.start_server(app)
	dash_duo.find_element("#visualization", timeout=10)

def test_choose_region_is_present(dash_duo):
	dash_duo.start_server(app)
	dash_duo.find_element("choose_region", timeout=10)
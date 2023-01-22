from flet import *
from recipe_scrapers import scrape_me

myscrapeweb = scrape_me("https://www.allrecipes.com/recipe/8513735/lemon-chicken-romano/")


def main(page:Page):
	# REMOVE PADDING OF YOU PAGE
	page.padding = 0 
	page.spacing = 0 
	page.scroll ="auto"
	mycolumn = ListView()
	detailfood = Column()
	nutritionfood = Column()


	# DETAILFOOD APPEND FROM WEBSCRAPPER

	for x in myscrapeweb.instructions_list():
		detailfood.controls.append(
			Column([
				Text(x)

				])


			)

	# NUTRITIONS

	for rr in myscrapeweb.nutrients():
		nutritionfood.controls.append(
		Container(
			bgcolor="green400",
			border_radius=30,
			padding=5,
			content=Row([
				Text(rr,color="white")

				])

			)


			)


	def animatescroll(e:ScrollEvent):
		# RUN YOU ANIMATE CHANGE BGCOLOR IF YOU SCROLL DOWN
		if e.local_y > 225:
			# EXAMPLE IF ABOVE 225 VALUE THEN RUN THIS ANIMATION
			print("YOU SCROLL > 225 VALUE !!!!")
			appbar.bgcolor = "blue"
			appbar.color="white"
			page.update()
		else:
			print("YOU SCROLL UNDER 225 VALUE !!!!")
			appbar.bgcolor = "white"
			appbar.color="black"
			page.update()



	# CREATE GESTURE DETECTOR FOR ANIMATE APPBAR
	gd = GestureDetector(
		on_scroll=animatescroll,
		drag_interval=50,
		content=Container(
			padding=10,
			content=Column([
			Text(myscrapeweb.title(),size=25,weight="bold"),
		Row([
			Text(f"{myscrapeweb.total_time()} minutes",size=14),
			Text(f"{myscrapeweb.yields()}",weight="bold",size=18),
		],alignment="spaceBetween"),
		Text("Intructions",size=25,weight="bold"),
		detailfood,

		Text("Nutritions",size=25,weight="bold"),
		nutritionfood,

		

				])

			)

		)

	mycolumn.controls.append(
		ResponsiveRow([
			Column([
			ShaderMask(
			Image(
			src=myscrapeweb.image(),
			fit="cover",
			width=page.window_width,
			height=300
				),
			blend_mode=BlendMode.DST_IN,
			# ADD EFFECT TRANSPARENT IN BOTTOM
			shader=LinearGradient(
				begin=alignment.top_center,
				end=alignment.bottom_center,
				colors=['white','transparent'],
				stops=[0.5,1]

				)
			),
			# ADD GESTURE FOR SCROLL ANIMATION 
			gd

				])
			])
		)

	# APPBAR ANIMATION ONSCROLL
	appbar = AppBar(
		title=Text(myscrapeweb.title(),size=20),
		bgcolor="white",
		leading=IconButton(icon="menu"),
		actions=[
			IconButton(icon="favorite"),
			IconButton(icon="more_vert"),

		]

		)

	# CREATE BOTTOM NAV FIXED ON SCROLLING
	bottombar = Container(
		bgcolor="orange",
		border_radius=30,
		bottom=page.window_width / 20,
		left=20,
		padding=5,
		right=20,
		content=Row([
			IconButton(icon="home",
			icon_size=30,
			icon_color="white"
			),
			IconButton(icon="favorite",
			icon_size=30,
			icon_color="white"
			),
			IconButton(icon="search",
			icon_size=30,
			icon_color="white"
			),
			IconButton(icon="settings",
			icon_size=30,
			icon_color="white"
			),

			],alignment="spaceBetween")

		)

	# ADD OVERLAY FIXED OF YOU BOTTOMBAR
	page.overlay.append(bottombar)

	page.add(
		appbar,
		Stack([
			mycolumn

			])

		)

flet.app(target=main)

import justpy as jp

from webapp import layout
from webapp import page


class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div,
               text="This is the about page!",
               classes="text-4xl m-2")
        jp.Div(a=div,
               text="""
               This is a webapp for a dictionary.
               Created as part of practice of the udemy course, Advanced Python by Example.
               """,
               classes="text-lg")
        return wp


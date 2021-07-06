import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
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


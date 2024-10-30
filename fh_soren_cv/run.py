from fasthtml import common as fh

from fh_soren_cv.data import Link, Project, links, projects

app, rt = fh.fast_app()


@rt("/")
def homepage():
    return fh.Titled(
        "Søren Vejlgaard Holm",
        fh.P(
            "MSc. in Engineering, Human-Centered Artificial Intelligence, Technical University of Denmark (DTU)"
        ),
        fh.P(
            "BSc. in Engineering, Artificial Intelligence and Data, DTU"
        ),
        fh.P("Machine Learning Engineer, Alvenir"),
        fh.P("Research Assistant, DTU Compute"),
        fh.H2("Projects"),
        fh.Table(
            *projects(),
        ),
        fh.H2("Links"),
        fh.Ul(
            *links(),
        ),
    )

@rt("/link")
def post(link: Link):
    return links.insert(link)

@rt("/project")
def post(project: Project):
    return projects.insert(project)


if __name__ == "__main__":
    fh.serve()

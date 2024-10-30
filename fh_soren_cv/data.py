from dataclasses import dataclass
from fasthtml import common as fh

from fh_soren_cv.infrastructure import LOCAL_DB_PATH

db: fh.Database = fh.database(LOCAL_DB_PATH)

@dataclass
class Link:
    id: int
    title: str
    url: str

    def __ft__(self):
        return fh.Li(
            fh.Th(fh.A(self.title, href=self.url)),
        )


@dataclass
class Project:
    id: int
    title: str
    url: str
    description: str
    organization: str

    def __ft__(self):
        return fh.Tr(
            fh.Th(self.title),
            fh.Th(self.description),
            fh.Th(fh.A(self.url, href=self.url)),
            fh.Th(self.organization),
        )

links = db.t.links if db.t.links in db.t else db.create(Link, pk="id")
projects = db.t.projects if db.t.projects in db.t else db.create(Project, pk="id")

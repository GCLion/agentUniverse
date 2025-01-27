from typing import Union
from pathlib import Path
from typing import List, Optional, Dict
import requests
from bs4 import BeautifulSoup

from agentuniverse.agent.action.knowledge.reader.reader import Reader
from agentuniverse.agent.action.knowledge.store.document import Document

class WebReader(Reader):
    """Web reader."""

    def _load_data(self, url: Union[str, Path], ext_info: Optional[Dict] = None) -> List[Document]:
        """Parse the webpage content.

        Note:
            `requests` and `BeautifulSoup` are required to read webpage content: `pip install requests beautifulsoup4`
        """
        try:
            if isinstance(url, Path):
                url = str(url)

            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            raise RuntimeError(
                f"Failed to fetch the webpage content from {url}. Error: {e}"
            )

        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string if soup.title else "Untitled"
        body_content = "\n".join(p.get_text(strip=True) for p in soup.find_all("p"))

        metadata = {"url": url, "title": title}
        if ext_info is not None:
            metadata.update(ext_info)

        return [Document(text=body_content, metadata=metadata or {})]

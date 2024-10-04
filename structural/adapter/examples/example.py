from ..pattern.abc import (
    AbstractAsyncDownloader,
    AbstractSyncDownloader,
)
from ..pattern.base import (
    BaseAsyncDownloader,
    BaseClient,
    BaseSyncDownloader,
    SyncResponse,
)


class AsyncToSyncAdapter(AbstractSyncDownloader):
    def __init__(self, downloader: AbstractAsyncDownloader) -> None:
        self._downloader = downloader

    def sync_download(self, urls: list[str]) -> list[SyncResponse]:
        async_responses = self._downloader.async_download(resources=urls)
        result = []
        for response in async_responses:
            result.append(
                SyncResponse(
                    resource=response['url'],
                    status_code=response['response_code'],
                    data=response['decoded_data'].encode(),
                )
            )

        return result


test_client = BaseClient()
sync_downloader = BaseSyncDownloader()
async_downloader = BaseAsyncDownloader()
sync_adapter = AsyncToSyncAdapter(downloader=async_downloader)

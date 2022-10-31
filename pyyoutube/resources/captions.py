"""
    Captions resource implementation
"""
from typing import Optional, Union

from pyyoutube.resources.base_resource import Resource
from pyyoutube.models import CaptionListResponse
from pyyoutube.utils.params_checker import enf_comma_separated, enf_parts


class CaptionsResource(Resource):
    """A caption resource represents a YouTube caption track

    References: https://developers.google.com/youtube/v3/docs/captions
    """

    def list(
        self,
        parts: Optional[Union[str, list, tuple, set]] = None,
        video_id: Optional[str] = None,
        id: Optional[Union[str, list, tuple, set]] = None,
        on_behalf_of_content_owner: Optional[str] = None,
        return_json: bool = False,
        **kwargs: Optional[dict],
    ) -> Union[dict, CaptionListResponse]:
        """Returns a list of caption tracks that are associated with a specified video.

        Args:
            parts:
                Comma-separated list of one or more caption resource properties.
            video_id:
                The parameter specifies the YouTube video ID of the video for which the API
                should return caption tracks.
            id:
                The id parameter specifies a comma-separated list of IDs that identify the
                caption resources that should be retrieved.
            on_behalf_of_content_owner:
                This parameter can only be used in a properly authorized request.
                Note: This parameter is intended exclusively for YouTube content partners.
            return_json:
                Type for returned data. If you set True JSON data will be returned.
            kwargs:
                Additional parameters for system parameters.
                Refer: https://cloud.google.com/apis/docs/system-parameters.

        Returns:
            Caption data
        """

        params = {
            "part": enf_parts(resource="", value=parts),
            "videoId": video_id,
            "id": enf_comma_separated(field="id", value=id),
            "onBehalfOfContentOwner": on_behalf_of_content_owner,
            **kwargs,
        }
        response = self._client.request(path="captions", params=params)
        data = self._client.parse_response(response=response)
        return data if return_json else CaptionListResponse.from_dict(data)

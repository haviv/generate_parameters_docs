# DownloadSFPicture

**Category:** User Management

**Description:** 

The DownloadSFPicture action automates the process of retrieving user photographs from SAP SuccessFactors, based on specified user IDs and photo types. This operation involves making a secure HTTPS request to the SuccessFactors API, downloading the picture data in a JSON format, and subsequently updating the user's photograph information in the ProfileTailor system. The action initiates by establishing a secured connection using TLS 1.2 protocol, authenticating with predefined credentials, constructing the API request with parameters provided by the user, and processing the response to update user properties in the ProfileTailor system with the downloaded photograph data.

**Parameters:** 

- Basic:
    - Name: sfUserId
    - Description: The unique identifier of the user in SAP SuccessFactors whose photo is to be downloaded.
    - Default value: None
    - Mandatory: Yes

    - Name: sfPhotoType
    - Description: The type of photograph to retrieve, indicating the specific photo category in SuccessFactors.
    - Default value: None
    - Mandatory: Yes

- Advanced:
    - Name: sfBaseUrl
    - Description: The base URL for the SAP SuccessFactors API. This parameter allows overriding the default API endpoint if needed.
    - Default value: "https://api10.successfactors.com/odata/v2/"
    - Mandatory: No

    - Name: adFieldsToUpdate
    - Description: Specifies the fields within the ProfileTailor system where the downloaded photo should be stored. This allows for custom mappings of photograph data to user properties.
    - Default value: "photo_jpegPhoto,photo_thumbnailPhoto"
    - Mandatory: No

**Business impact:** 

This action streamlines the process of synchronizing user photographs between SAP SuccessFactors and the Pathlock cloud system, enhancing the user experience by ensuring that current and consistent user photographs are displayed within the system. It aids in maintaining an updated visual representation of users, which can be crucial for identification in security contexts and for personalization of the user interface. 

**Example of usage:** 

In a scenario where a company's HR system updates an employee's photograph in SuccessFactors, this action can be triggered to automatically update the user's photo in the Pathlock cloud. This ensures that the most recent photograph is used across all platforms without manual intervention, maintaining consistency and enhancing security and user experience.

**Prerequisites:** 

- The user must have valid credentials (userName, password) for SAP SuccessFactors.
- The WorkflowInstance and the ProfileTailorContext must be properly initialized and configured with access to the SAP SuccessFactors API.
- Proper configuration in Pathlock with access rights to perform HTTP requests to external systems such as SuccessFactors.

**Error Handling and Troubleshooting:** 

- **Error:** "Download SFPicture returned empty"
    - **Cause:** This may occur if the user ID or photo type does not exist in SuccessFactors, the API endpoint is incorrect, or there were issues in the network request.
    - **Solution:** Verify the user ID and photo type parameters, check the base URL for the SuccessFactors API, and ensure network connectivity.
    
- **Error:** Exception during the API request
    - **Cause:** Could be due to incorrect credentials, network issues, or changes in the API endpoint or response format.
    - **Solution:** Check the credentials used for the SuccessFactors API request. Confirm the base URL and API endpoint availability and response format. In case of network issues, ensure connectivity and proper configuration of security protocols.
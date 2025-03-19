# DownloadFileAction

**Category:** Workflow

**Description:**  
The DownloadFileAction is designed to download files from specified URLs, validate these files, and manage retries in case of failures. The action splits the provided file URLs, attempts to download each file while respecting the designated timeout and number of retries settings. Post-download, it validates the file format and content type against known secure file types, then stores the validated file in a database and on the server. This process is crucial for ensuring that only safe and relevant files are processed and stored, maintaining the integrity and security of the system.

**Parameters:**  
- **Basic Parameters:**
  - Name: DownloadUrlField
    Description: Comma-separated URLs from which files will be downloaded.
    Default value: None
    Mandatory: yes
  - Name: DownloadNumberOfRetryField
    Description: Specifies the number of retries for downloading the file if the first attempt fails.
    Default value: 1
    Mandatory: no

- **Advanced Parameters:**
  - Name: DownloadTimeoutField
    Description: Timeout duration in seconds for the download attempt.
    Default value: 20
    Mandatory: no
  - Name: SecurityProtocolType
    Description: The security protocol type to be used for the download request. Defaults to TLS 1.2 if not specified or invalid.
    Default value: TLS12
    Mandatory: no

**Business impact:**  
This action automates the retrieval and validation of files necessary for processes like Privileged Access Management (PAM), access control, and risk calculation. By ensuring that only valid and intended files are downloaded and preserved, it plays a pivotal role in safeguarding the system against unauthorized access and malware. This enhances overall system security, aids in compliance and risk management, and ensures that self-service requests are handled efficiently and securely.

**Example of usage:**  
One possible use case for the DownloadFileAction could be during an automated process for updating user permissions based on their current roles or requisitions. Before applying the updates, the system might need to download and validate specific configuration files from a secure location. This action can be configured to download these files, validate them, and proceed only if the files are safe and meet the predefined criteria, automating a critical part of the workflow with added security measures.

**Prerequisites:**  
- User must have network access to the specified URL(s).
- Sufficient permissions to write to the database and server where files are stored.
- The system should be configured to use a supported security protocol for file downloads.

**Error Handling and Troubleshooting:**  
- If a file fails to download after the specified number of retries, an error message detailing the failed URL and the error will be logged.
- Timeout errors might suggest network issues or incorrect URL formatting; verifying the URL and network status can help resolve these issues.
- Security protocol mismatch or misconfiguration could result in download failures, ensure the security protocol parameter matches the server's configuration.
- Invalid file types or corrupt files will result in validation errors. Verify the file source and type if such errors arise.

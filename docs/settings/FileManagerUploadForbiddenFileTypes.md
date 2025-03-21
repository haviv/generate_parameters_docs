**File Manager Upload Forbidden File Types**

**Technical Name:** FileManagerUploadForbiddenFileTypes

**Category:** Security

**Default Value:** (Not provided in the code references)

**Impact Level:** High

**Description:**

This parameter defines the types of files that are not allowed to be uploaded to the Pathlock Cloud GRC platform through the File Manager. It is utilized to prevent unauthorized or potentially dangerous file types from compromising the system's security.

**Business Impact:**

Setting the File Manager Upload Forbidden File Types ensures that only authorized file formats are uploaded, mitigating the risk of malware, data breaches, and other security threats. This configuration protects sensitive compliance and risk management data, thereby supporting the organization's overall security posture.

**Technical Impact when configured:**

When configured, this parameter actively blocks any attempt to upload files that match the forbidden types, ensuring that only files of allowed types can be uploaded. This filtering helps in maintaining the integrity and security of the data stored within the Pathlock platform.

**Examples Scenario:**

An organization wishes to prohibit the upload of executable files (.exe) to prevent the risk of software running that could potentially harm the system or compromise data. By including ".exe" in the FileManagerUploadForbiddenFileTypes, the system will automatically block any upload attempts of these file types.

**Related Settings:**

(No directly related settings provided in the code references)

**Applicable Workflows Actions:** 

(No specific workflow actions mentioned for this parameter in the code references)

**Best Practices:** configure when you are looking to enforce file upload restrictions based on the file type to enhance security. Avoid when there's a need for flexibility in file uploads without compromising system security through other means.
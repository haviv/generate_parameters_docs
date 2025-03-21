# Virtual Profile Pictures Folder Path

**Technical Name:** VirtualProfilePicturesFolderPath

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

Specifies the path to a virtual directory where user profile pictures are stored. This setting is critical for the correct display and management of user avatars across the Pathlock GRC platform. 

**Business Impact:**

Ensuring that this path is correctly configured allows for a cohesive user experience, contributing to easier identification of users within the system. It enhances the visual aspect of user management and facilitates smoother interactions within the platform, particularly in modules that rely on visual identification.

**Technical Impact when configured:**

Proper configuration ensures seamless access and display of user profile pictures. Incorrect configuration can lead to broken or missing avatar images, affecting the usability and aesthetic of the user interface.

**Examples Scenario:**

- **Scenario:** An organization wants to migrate their user profile pictures to a new server location. By updating the `VirtualProfilePicturesFolderPath` to the new path, all user profiles on the Pathlock GRC platform will automatically reference pictures from the new location without needing to update each user profile individually. 

**Related Settings:**

- `CommonSettings.Default.RolesRegistryNodes`
- `CommonSettings.Default.RunReportOnStart`

**Best Practices:** 

- **Configure when** setting up or migrating the platform to ensure that the path reflects the current or new storage location for profile pictures.
- **Avoid when** the default configuration aligns with the organization's current storage setup or when changes to the storage path could disrupt access to existing profile images.
# PTDM Logo Html Path

**Technical Name:** PTDM_LogoHtmlPath

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The PTDM_LogoHtmlPath parameter is utilized to specify the file path for a custom HTML logo within the Pathlock GRC platform. This configuration allows organizations to personalize their GRC environment with a custom logo, enhancing the platform's alignment with the organization's branding guidelines.

**Business Impact:**

Customizing the logo via the PTDM_LogoHtmlPath parameter enhances the user experience by reinforcing brand identity and promoting a seamless integration with other organizational tools and platforms. It fosters a sense of familiarity and professionalism among users, potentially increasing engagement with the GRC platform.

**Technical Impact when configured:**

When configured, this parameter directs the Pathlock GRC platform to load a custom HTML file as the logo instead of the default logo. This allows for a higher degree of customization, including the use of complex logos and branding elements that might not be possible through standard image formats.

**Examples Scenario:**

An organization wants to update their GRC platform's interface to include their newly rebranded logo, which includes dynamic elements such as animated parts or interactive elements. By configuring the PTDM_LogoHtmlPath to point to their custom-designed HTML file, they can achieve this level of customization, ensuring the platform reflects the new brand identity accurately.

**Related Settings:**

- PTDM_LogoPath

**Best Practices:** 

- **Configure when:** you need to enhance the branding of your Pathlock GRC platform beyond what's possible with standard image formats, especially to include dynamic or interactive logo elements.
  
- **Avoid when:** you are not prepared to ensure that the custom HTML logo meets accessibility and responsiveness criteria across all devices used to access the Pathlock GRC platform.
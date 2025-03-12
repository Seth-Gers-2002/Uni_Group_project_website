As a [Description of user], professional cleaner
I want [functionality], the ability to see the location of the job on the map/GPS
so that [benefit], it's easier to find and plan out how to travel to the location

prioities from the user story
10: the ability to copy the address for gps and maps
40: a pre-image of the location from google maps on website

# User story title: Map to location

## Priority: 40
Could have:
That on the job details there is a section that displays the address using a GPS or satellite 


## Estimation: e.g. 2 days
Any notes on estimation go here. Keep your planning poker game numbers. For example
* Aaron: 1 day
* Seth: x
* Harrison: 1 day


## Assumptions (if any):

## Description: e.g. The web page will show current deals to Orion's orbits users

Description-v1: e.g A section that displays the address AND show it on a map or GPS 
# User story title: Map to location

## Priority: 40
Could have:
A section within the job details that displays the address along with a map view (or satellite view) from Google Maps. Additionally, users should have the ability to copy the address for use in external GPS apps or maps.

## Estimation: e.g. 2 days
Any notes on estimation:
* Aaron: 3 days
* Seth: 2 days
* Harrison: 3 days

## Assumptions (if any):
- The web application has access to the Google Maps API or an equivalent mapping service.
- Job details include a valid address that can be geocoded.
- Users have internet connectivity to load the map view.
- The feature is primarily for professional cleaners who need quick directions to the job site.

## Description:
The web page or job details section will show the physical address of the job along with an embedded map view. This allows the cleaner to see the location visually via GPS/satellite imagery. Additionally, there is functionality to copy the address directly for use in external navigation applications.

Description-v1:
A dedicated section in the job details that displays the job address and a pre-rendered image (or live map embed) from Google Maps, enabling professional cleaners to quickly plan and navigate to the location. A copy-to-clipboard button is provided for the address to facilitate easy transfer to external GPS/navigation tools.

## Tasks, see chapter 4:
- Integrate with the Google Maps API to fetch and display the location map based on the job address.
- Develop the UI component for showing the pre-image/map view.
- Implement a copy-to-clipboard functionality for the address.
- Ensure that fallback behavior is in place if the map cannot be loaded (e.g., display a static image or error message).
- Test the functionality across different devices and browsers for consistency and reliability.

# UI Design:
- A clear and prominent section within the job details page that shows:
  - The address text with a copy icon/button.
  - An embedded map or a pre-rendered image of the location.
  - A responsive design that adjusts for mobile and desktop views.

# Completed:
(Not completed)

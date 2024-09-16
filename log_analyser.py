import re  # Import regular expression module to find patterns in log lines
from collections import Counter  # Import Counter to count occurrences

# Function to read the log file
def parse_log(file_path):
    with open(file_path, 'r') as log_file:
        logs = log_file.readlines()  # Read all lines of the log file
    return logs  # Return the list of log lines

# Function to extract and analyze information from logs
def analyze_logs(logs):
    status_codes = []  # List to store all status codes
    requested_pages = []  # List to store all requested pages
    ip_addresses = []  # List to store all IP addresses

    # Process each line in the log file
    for log in logs:
        # Use regex to match the pattern and extract the required parts
        log_pattern = re.match(r'(\S+) \S+ \S+ \[.*?\] "\S+ (\S+) \S+" (\d+) \S+', log)
        
        if log_pattern:  # If the line matches the pattern
            ip_address, requested_page, status_code = log_pattern.groups()
            status_codes.append(status_code)  # Add status code to list
            requested_pages.append(requested_page)  # Add requested page to list
            ip_addresses.append(ip_address)  # Add IP address to list

    return status_codes, requested_pages, ip_addresses  # Return the data we extracted

# Function to generate a summary report
def generate_report(status_codes, requested_pages, ip_addresses):
    # Count the number of 404 errors
    print(f"Total 404 Errors: {Counter(status_codes)['404']}")
    
    # Find the top 5 most requested pages
    print("\nTop 5 Requested Pages:")
    for page, count in Counter(requested_pages).most_common(5):
        print(f"{page}: {count} requests")

    # Find the top 5 IP addresses making the most requests
    print("\nTop 5 IPs with most requests:")
    for ip, count in Counter(ip_addresses).most_common(5):
        print(f"{ip}: {count} requests")

# Main function to tie everything together
def main():
    # Parse the log file (replace 'webserver.log' with your log file path)
    logs = parse_log('sample_log.txt')
    
    # Analyze the logs to extract information
    status_codes, requested_pages, ip_addresses = analyze_logs(logs)
    
    # Generate the final report
    generate_report(status_codes, requested_pages, ip_addresses)

# Call the main function when the script is run
if __name__ == "__main__":
    main()

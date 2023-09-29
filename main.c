// Implementation of HTTP request in c language

#include<stdio.h>
#include<curl/curl.h>

int main(int argc, char const *argv[])
{
	CURL *curl;
	CURLcode result;

	curl = curl_easy_init();

	if (curl == NULL) {
		fprintf(stderr, "%s\n", "HTTP Request failed\n");
		return -1;
	}

	curl_easy_setopt(curl, CURLOPT_URL, "http://localhost:5000/getOrders");
	result = curl_easy_perform(curl);

	if (result != CURLE_OK) {
		fprintf(stderr, "Error: %s\n", curl_easy_strerror(result));
		return -1;
	}

	curl_easy_cleanup(curl);
	return 0;
}

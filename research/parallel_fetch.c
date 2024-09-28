#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <opencv2/opencv.hpp>

#define MAX_THREADS 5
#define BUFFER_SIZE 1024
#define IMAGE_DISPLAY_DURATION 3000  // in milliseconds

pthread_mutex_t lock;

typedef struct {
    char letter;
} ThreadData;

void *display_image(void *arg) {
    ThreadData *data = (ThreadData *)arg;
    char filename[50];
    snprintf(filename, sizeof(filename), "path_to_sign_language_images/%c.jpg", data->letter);

    cv::Mat img = cv::imread(filename, cv::IMREAD_COLOR);
    if (img.empty()) {
        fprintf(stderr, "Could not open or find the image for letter %c\n", data->letter);
        free(data);
        pthread_mutex_unlock(&lock);
        return NULL;
    }

    cv::imshow(&data->letter, img);
    cv::waitKey(IMAGE_DISPLAY_DURATION);
    cv::destroyWindow(&data->letter);

    free(data);
    pthread_mutex_unlock(&lock);
    return NULL;
}

void handle_file(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Could not open file");
        return;
    }

    char buffer[BUFFER_SIZE];
    pthread_t threads[MAX_THREADS];
    int thread_index = 0;

    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("Read from file: %s\n", buffer);

        for (int i = 0; i < strlen(buffer); ++i) {
            if (buffer[i] != '\n' && buffer[i] != '\r' && buffer[i] != ' ') {
                pthread_mutex_lock(&lock);
                ThreadData *data = (ThreadData *)malloc(sizeof(ThreadData));
                data->letter = toupper(buffer[i]);

                pthread_create(&threads[thread_index], NULL, display_image, data);
                pthread_detach(threads[thread_index]);

                thread_index = (thread_index + 1) % MAX_THREADS;
            }
        }
    }

    fclose(file);
}

int main() {
    pthread_mutex_init(&lock, NULL);

    // Replace "input.txt" with the path to input text file
    handle_file("input.txt");

    pthread_mutex_destroy(&lock);

    return 0;
}

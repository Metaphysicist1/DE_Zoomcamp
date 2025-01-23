# NY-Taxi Data Analyzer

## Project Description
The NY-Taxi Data Analyzer is a project designed to facilitate the analysis of New York City taxi data using PostgreSQL and PgAdmin. This project leverages Docker to create a containerized environment for easy setup and management of the database.

![image](https://github.com/user-attachments/assets/8357f239-29cd-4694-a11d-0e3d18f6da21)



## Setup Instructions

 **If Prefare Pull Ingest Data Image from Docker Hub**
   ```bash
   docker pull metaphysicist/postgres-ingest
   ```


1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ny-taxi-data-analyzer.git
   cd ny-taxi-data-analyzer
   ```

2. **Pull the Docker Images**
   Pull the necessary Docker images for PostgreSQL and PgAdmin:
   ```bash
   docker pull postgres
   docker pull dpage/pgadmin4
   ```

3. **Run Docker Containers**
   Start the PostgreSQL and PgAdmin containers using Docker Compose:
   ```bash
   docker-compose up -d
   ```

4. **Access PgAdmin**
   Open your web browser and navigate to `http://localhost:5050`. Log in with the credentials specified in your `docker-compose.yml` file.

5. **Connect to PostgreSQL**
   In PgAdmin, create a new server connection using the following details:
   - **Host**: `postgres`
   - **Port**: `5432`
   - **Username**: `your_postgres_user`
   - **Password**: `your_postgres_password`

## Usage
Once connected, you can start analyzing the NY-Taxi data. Import your dataset into the PostgreSQL database and use SQL queries to extract insights.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the contributors and the open-source community for their support.


# Accessing GEO data through PEPhub

Moreover, users can download all project as `tar file` from the GEO namespace using the link available on the geo namespace page. PEPhub doesn't store actual files in the database. Because of this, if you want to download files, there are two options:

 - Use links to the files that are stored in the project sample table.
 - Use geofetch on a local machine to download these files.
Example: `geofetch -i GSE95654 --processed`, where `--processed` indicates that you want to download processed data, not SRA. More information about PEP can be found on the official website [GEOfetch](https://geofetch.databio.org/en/latest/).

# BMS-Dashboard
Timeline & Inventory Tracking  Dashboard


## Aim of the Project

This project aims to provide an Internal Systems Dashboard for BITS Motorsports

## This Dashboard Can

1. Create a Task & Store It 
2. Display Items in the Inventory
3. Show the Project Timeline

## License

[MIT](https://choosealicense.com/licenses/mit/)

- Please Note Only BMS Documentation Team Members Can Use this Dashboard For Now## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Primary Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Secondary Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Tertiary Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Accent Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Used By

This project is used by the following companies:

- BITS Motorsports


## Deployment

To deploy this project run

```bash
  streamlit run streamlit_app.py
```


## Documentation

[Documentation](https://linktodocumentation)


![Logo](https://www.google.com/url?sa=i&url=https%3A%2F%2Fin.linkedin.com%2Fcompany%2Farc-motors%3Ftrk%3Dpublic_profile_experience-item_profile-section-card_image-click&psig=AOvVaw0rzFT8mpZKUJaTyi2zD_B4&ust=1686156820015000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCLDCsfSNr_8CFQAAAAAdAAAAABAI.png)


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.



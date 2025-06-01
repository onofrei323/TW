# Inventory Management System

A comprehensive Flask web application for warehouse inventory management with consumption bill tracking and reception management.

## Features

- **Product Management**: Add, edit, delete products with stock tracking
- **Consumption Bills**: Create consumption bills to track outgoing inventory
- **Reception Sheets**: Record incoming inventory from suppliers
- **Low Stock Alerts**: Dashboard shows products below minimum stock levels
- **Excel Export**: Export bills and reception sheets to Excel format
- **Draft System**: Save incomplete bills and receptions as drafts
- **PostgreSQL Database**: Reliable database with proper relationships

## Deployment on Render.com

### Quick Deploy

1. Fork this repository to your GitHub account
2. Go to [Render.com](https://render.com) and sign up/login
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Use these settings:
   - **Environment**: Python
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`

### Database Setup

The `render.yaml` file will automatically create a PostgreSQL database for you. Render will:
- Create a free PostgreSQL instance
- Set up the `DATABASE_URL` environment variable
- Initialize the database tables on first deployment

### Environment Variables

The following environment variables will be automatically configured:
- `DATABASE_URL`: PostgreSQL connection string (auto-generated)
- `SESSION_SECRET`: Flask session secret (auto-generated)
- `PORT`: Application port (set by Render)

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up PostgreSQL database and environment variables:
   ```bash
   export DATABASE_URL="postgresql://username:password@localhost/inventory_db"
   export SESSION_SECRET="your-secret-key"
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Usage

- **Dashboard**: View low stock alerts and recent activity
- **Products**: Manage your inventory items
- **Consumption Bills**: Track items taken from inventory
- **Reception**: Record new inventory arrivals
- **Export**: Download Excel reports for bills and receptions

## Romanian Interface

The interface is in Romanian as per the original desktop application:
- Produse (Products)
- Bonuri de Consum (Consumption Bills)
- Fișe de Recepție (Reception Sheets)
- Stoc Minim (Minimum Stock)
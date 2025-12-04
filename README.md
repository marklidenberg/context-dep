# dep

Embarassingly simple Python dependency injection.

## Usage

```python
from dep import dep, override

@dep()
def get_db():
    db = Database()
    yield db
    db.close()

with get_db() as db:
    db.query(...)

# Async support
@dep()
async def get_async_db():
    db = await AsyncDatabase()
    yield db
    await db.close()

async with get_async_db() as db:
    await db.query(...)

# Override for testing
@dep()
def get_mock_db():
    yield MockDatabase()

override({get_db: get_mock_db})
```

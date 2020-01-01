::Update Maverick and Commit Changes

call setss

git pull

git submodule update --init --recursive
cd Kepler
git pull origin master --rebase

cd ..
git add .
git commit -m "Update Kepler"
git push

pause
